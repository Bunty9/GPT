from github import Github
import time
from datetime import datetime
import os
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, cyan


end_time = 1614284643
start_time = end_time - 86400

ACCESS_TOKEN = open("token.txt", "r").read()
g = Github(ACCESS_TOKEN)
print(g.get_user())

# query = "language:python"
# result = g.search_repositories(query)

# print(result.totalCount)
# print(dir(result))

for i in range(3):
    try:
        start_time_str = datetime.utcfromtimestamp(
            start_time).strftime('%Y-%m-%d')
        end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
        query = f"language:python created:{start_time_str}..{end_time_str}"
        # print(query)
        end_time -= 86400
        start_time -= 86400

        result = g.search_repositories(query)
        print(result.totalCount)

        for repository in result:
            # print(f"{repository.git_url}")
            print(f"{repository.clone_url}")
            # print(f"{repository.owner.login}")
            # print(dir(repository))

            os.system(
                f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}"
            )
            print(cyan(f"current start time ...::{start_time}"))
            # break
    except Exception as e:
        print(str(e))
        print(red("..... BROKE FOR SOME REASON ....."))
        time.sleep(120)


print(green(f"finished, your new end time is ..:: {start_time} "))
