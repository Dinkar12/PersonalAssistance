from output_module import output
from time_module import get_time, get_date
from input_module import take_input
from database import *
from internet import check_internet_connection, check_on_wikipedia
import assistant_details
from web_jobs import open_google, open_facebook, close_browser
from news_module import get_news


def process(query):
    answer = get_answer_from_memory(query)

    if answer == "":
        output("Dont know this one should i search on internet?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer

    if answer == "get time details":
        return "Time is " + get_time()
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    elif answer == "tell date":
        return "Date is " + get_date()

    elif answer == "on speak":
        return turn_on_speech()

    elif answer == "off speak":
        return turn_off_speech()

    elif answer == "close browser":
        close_browser()
        return "closing browser"

    elif answer == "open facebook":
        open_facebook()
        return "opening facebook"

    elif answer == "open google":
        open_google()
        return "opening google"

    elif answer == "get news":
        return get_news()

    elif answer == 'change name':
        output("Okay! what do you want to call me")
        temp = take_input()
        if temp == assistant_details.name:
            return "can't change. I think you're happy with my old name"
        else:
            update_name(temp)
            assistant_details.name = temp
            return "Now you can call me " + temp
    else:
        output("Dont know this one should i search on internet?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else:
            output("can you please tell me what it means?")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "")
                ans = ans.strip()

                value = get_answer_from_memory(ans)
                if value == "":
                    return "can't help with this one"
                else:
                    insert_question_and_answer(query, value)
                    return "Thanks i will remember it for the next time"

            else:
                return "can't help with this one"
