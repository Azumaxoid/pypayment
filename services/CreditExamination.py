from . import LowAmountExamination
from . import HighAmountExamination
import newrelic.agent

@newrelic.agent.function_trace()
def exam(card, total) :
    if total <= 100:
      return LowAmountExamination.exam(card, total)
    if total > 100:
      return HighAmountExamination.exam(card, total)

