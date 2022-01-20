import time
import newrelic.agent

@newrelic.agent.function_trace()
def exam(card, total) :
    return check(total)

@newrelic.agent.function_trace()
def check(total):
    for num in range(0, 100, 10) :
      if _check(total, num) :
        return True
    return True

@newrelic.agent.function_trace()
def _check(total, num):
    time.sleep(0.3)
    return total < num
