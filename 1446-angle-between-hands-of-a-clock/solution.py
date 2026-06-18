class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:


        minuteHand = (minutes/60) * 360
        hourHand = ((hour%12)/12 + (minutes/60)/12) * 360 

        return min(abs(minuteHand - hourHand), 360 - abs(hourHand - minuteHand))


