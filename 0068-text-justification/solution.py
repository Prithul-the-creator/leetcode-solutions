class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:




        result = []

        currentLine = []
        currentLineLength = 0


        for word in words:


            if currentLineLength + len(word) + len(currentLine) <= maxWidth:

                currentLine.append(word)
                currentLineLength += len(word)

            else:

                result.append((currentLine, currentLineLength))
                currentLine = [word]
                currentLineLength = len(word)
        
        final = []

        for line, length in result:
            

            spaces = maxWidth - length

            if len(line) == 1:
                final.append(line[0] + spaces * " ")
                continue

            equalspace = spaces // (len(line) - 1)
            leftover = spaces % (len(line) - 1)
            

            finalline = ""
            for word in line[:-1]:
                if leftover > 0:
                    finalline += word + (equalspace * " ") + " "
                else:
                    finalline += word + (equalspace * " ")
                leftover -= 1
            finalline += line[-1]
            final.append(finalline)
        
        spaces = maxWidth - currentLineLength - (len(currentLine) - 1)
        lastline = ""
        for word in currentLine:
            lastline += word + " "
        lastline = lastline[:-1] + spaces * " "
        final.append(lastline)

        return final
