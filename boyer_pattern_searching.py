class PatternSearching:

    def __init__(self, text):
        self.text = text

    def search(self, pattern):
        print(self.text)
        print(pattern)
        index = -1
        t_index = len(pattern) - 1
        while t_index < len(self.text):
            diff_index = self.difference_index(pattern, t_index)
            print("diff_index = " + str(diff_index) + " t_index = " + str(t_index))
            if diff_index == -1:
                index = t_index - (len(pattern)-1)
                break
            p_index = self.char_position_in_pattern(pattern, self.text[diff_index])
            print("p_index = " + str(p_index) + "char = " + str(pattern[p_index]))
            if p_index == -1:
                t_index = t_index + len(pattern)
            else:
                #t_index =  diff_index + t_index - p_index
                t_index = t_index + p_index
                print("incr pos = " + str(t_index))
        return index

    def difference_index(self, pattern, end_index):
        offset = len(pattern)

        i = offset - 1
        while i > -1:
            if self.text[end_index] != pattern[i]:
                return end_index; 
            end_index = end_index - 1
            i = i - 1
        return -1

    def char_position_in_pattern(self, pattern, c):
        try:
            return pattern.rindex(c)
        except ValueError:
            return -1


pattern_searching = PatternSearching("dfManishddfad")

print("index = " + str(pattern_searching.search("Manish")))
#print("index = " + str(pattern_searching.search("nis")))
