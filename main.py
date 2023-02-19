import asyncio

import googlemaps
import googlemaps.places

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')


# 요청은 동기 형태로 처리된다. -> run_in_executor()를 이용해서 보내면 될 듯. 비동기를 지원하지 않기 때문
def get_map_data(posi):
    pass

def result_to_dict(my_dict, result):
    pass

# 포지션을 나눠서 각 위도, 경도를 구하는 작업이 필요하다. (함수가 필요함)

# 여기서는 API를 이용해서 데이터만 불러오면 된다.
async def main():
    loop = asyncio.get_running_loop()
    # 음식점 저장 자료구조
    my_dict = dict()
    executor_future = [loop.run_in_executor(None, get_map_data, posi) for posi in posi_list]
    result = await asyncio.gather(*executor_future, return_exceptions=True)
    result_to_dict(my_dict, result)
    return my_dict


# 불러온 데이터는 파일에 일단 적히면 된다.
# 파일에 다 기록되었으면, 파일을 읽어와서 Key - Value 형태로 압축되면 된다. 이 때 Key는 가게명 + 주소명.
# 파일에는 존재하지만, 구글에서 새로 불러왔을 때 없는 녀석이 있을 수 있다. 이 경우는 어떻게 처리하는게 맞을까?
# 항상 전체가 Scan 되기 때문에 구글에서 새로 불러온 녀석을 기준으로 하는게 맞다.
# DB에는 항상 업데이트 한 시간을 기록한다. 마지막에 업데이트 된 시간이 이것보다 작은 녀석은 폐업() 같은 것들로 표기해준다.


googlemaps.places.places_nearby(
    client=gmaps,
)
googlemaps.places.find_place(
    client=gmaps,
)
