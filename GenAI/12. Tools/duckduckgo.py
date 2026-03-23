from langchain_community.tools import DuckDuckGoSearchRun
search_net = DuckDuckGoSearchRun()

result = search_net.invoke('ipl 2026')

print(result)