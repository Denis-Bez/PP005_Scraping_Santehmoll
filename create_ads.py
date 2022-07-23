# Class Contains methods for generation Yandex Direct's API requests
from Class_API_Yandex import API_Requests

# 439291
# 439290
# Д.б. проверка на количество групп в компании. Если больше 1000, то новая компания. Учитывать и архивные компании


def request_api():

    ReqYandex = API_Requests()
    # print(ReqYandex.getCampaigns())
    # print(ReqYandex.deleteCampaign(439292))
    print(ReqYandex.GroupsCount(439291))



if __name__ == "__main__":
    request_api()