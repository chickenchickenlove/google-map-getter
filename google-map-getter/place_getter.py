import googlemaps
import contextlib
import asyncio
from googlemaps import places


FIND_TYPE = 'restaurant'
RADIUS = 10000

@contextlib.contextmanager
def get_gmaps_client(api_key):
    gmap = googlemaps.Client(key=api_key)
    try:
        yield gmap
    finally:
        print('gmaps closed')


def transfer_dict(ret_dict, response_list):

    # name, rating, vicinity
    # key = name + vicinity
    # value = (name, rating, vicinity)
    for response_dict in response_list:
        name = response_dict['name']
        vicinity = response_dict['vicinity']
        rating = 0 if 'rating' not in response_dict else response_dict['rating']

        key = name + '/' + vicinity
        value = (name, vicinity, rating)

        ret_dict[key] = value


async def get_place_data(api_key, cur_location, radius, find_type):
    ret_dict = dict()
    next_page_token = -1

    with get_gmaps_client(api_key) as client:
        while next_page_token is not None:
            await asyncio.sleep(2)
            # {'html_attributions': [], 'results': [], 'status': 'ZERO_RESULTS'}
            # {'html_attributions': [], 'results': [dict1, dict2, ...], 'status': 'OK'}
            if next_page_token == -1:
                result_dict = client.places_nearby(
                    location=cur_location,
                    radius=radius,
                    language='ko',
                    type=find_type,
                    keyword='맛집')
            else:
                result_dict = client.places_nearby(
                    location=cur_location, page_token=next_page_token)

            # result_dict : dict
            # result_dict['results'] : [dict, dict, dict, ...]
            response_list = result_dict['results']
            # TODO : status ok
            transfer_dict(ret_dict, response_list)

            next_page_token = None if 'next_page_token' not in result_dict else result_dict['next_page_token']
            print('KKKK')


    return ret_dict


async def place_getter_main_async(api_key, position_list):

    result_dict = dict()

    radius = RADIUS
    find_type = FIND_TYPE

    loop = asyncio.get_running_loop()

    # asyncio.create_task(get_place_data(api_key, ))

    tasks = [asyncio.create_task(get_place_data(
        api_key, cur_location, radius, find_type)) for cur_location in position_list]
        # None,
        # get_place_data,
        # api_key,
        # cur_location,
        # radius,
        # find_type) for cur_location in position_list]

    await asyncio.sleep(1)

    results = [await t async for t in tasks]
    # for t in tasks:
    #     r = await t
    #     print(r)
        # print(loop.run_until_complete(t))


    # for f in futures:
    #     loop.run_until_complete(f)
    #     # await f
    #
    # group = asyncio.gather(*futures, return_exceptions=True)
    # for t in futures:
    #     r = loop.run_until_complete(t)
    # response = loop.run_until_complete(futures)


    # for partial_result in response:
    #     for key, value in partial_result:
    #         result_dict[key] = value

    return result_dict



def place_getter_main(api_key, position_list):

    # loop = asyncio.get_running_loop()
    # futures = [loop.run_in_executor(None, get_place_data, api_key, cur_location, radius, find_type) for cur_location in position_list]
    # get_place_data(api_key)
    #
    # group = asyncio.gather(*futures, return_exceptions=True)
    # loop.run_until_complete(group)



    cur_location = position_list.pop()

    get_place_data(api_key, cur_location, RADIUS, FIND_TYPE)
    print(2)

