import time
import newrelic.agent

@newrelic.agent.function_trace()
def exam(card, total):
    checkLastActivity(card)
    return checkAmount(card, total)

@newrelic.agent.function_trace()
def expired(card):
    time.sleep(0.05)
    return False

@newrelic.agent.function_trace()
def checkLastActivity(card):
    expired(card)
    for num in range(10):
        checkActivity(card)
    return True

@newrelic.agent.function_trace()
def checkActivity(card):
    expired(card)
    return True


@newrelic.agent.function_trace()
def checkAmount(card, total):
    for limit in range(1000, 200, -10):
      if check(card, total, limit):
        return False
    raise Exception('Amount Examination Failed. Please check payment gateway')

@newrelic.agent.function_trace()
def check(card, total, limit):
    expired(card)
    return total > limit
