class Solution {

    fun nWhitespace(n: Int): CharArray = CharArray(n){' '}

    fun mergeWordLinesToStrings(words: List<String>, wordsLenSum: Int, maxWidth: Int, isLastLine: Boolean): String {
        val wsCount = maxWidth - wordsLenSum
        var sb = StringBuilder(words.first())

        if(words.size == 1 || isLastLine){
            for(i in 1 until words.size) {
                sb.append(' ')
                sb.append(words[i])
            }
            sb.append(nWhitespace(wsCount - (words.size - 1)))
            return sb.toString()
        }

        val wsMinSize = wsCount / (words.size - 1)
        val numWordsWithLongWs = wsCount % (words.size - 1)
        val wsShortStr = nWhitespace(wsMinSize)
        val wsLongStr = nWhitespace(wsMinSize + 1)

        for(i in 1 until words.size) {
            val ws = if(i <= numWordsWithLongWs) wsLongStr else wsShortStr
            sb.append(ws)
            sb.append(words[i])
        }
        return sb.toString()
    }


    fun fullJustify(words: Array<String>, maxWidth: Int): List<String> {
        val wordLines: MutableList<String> = mutableListOf()
        var line: MutableList<String> = mutableListOf()

        var wordIndex = 0
        var lineWordsLenSum = 0

        var i = 0
        while(i < words.size){
            val word = words[i]
            if(word.length + lineWordsLenSum + wordIndex <= maxWidth) {
                line.add(word)
                wordIndex++
                lineWordsLenSum += word.length
                i++
            } else {
                wordLines.add(mergeWordLinesToStrings(line, lineWordsLenSum, maxWidth, false))
                line = mutableListOf()
                lineWordsLenSum = 0
                wordIndex = 0
            }
        }
        wordLines.add(mergeWordLinesToStrings(line, lineWordsLenSum, maxWidth, true))

        return wordLines
    }
}
