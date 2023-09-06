class AutoCell:
    def __init__(self, lin0='00001000', rule_num=30):
        self.lin0 = lin0
        self.__rule_num = rule_num

    @property
    def rule_num(self):
        return self.__rule_num
        
    @rule_num.setter
    def rule_num(self, value):
        if value>256 or value<1:
            print('Value must be between 1 and 256, inclusive!')
            print('###\nSetting it default Rule 30 \n###')
            self.__rule_num = 30
        else:
            self.__rule_num = value
    
    def rule(self):
        num = self.rule_num
        patterns = {}
        pattern_list = ['000', '001', '010', '011', '100', '101', '110', '111']
        for i in range(7, -1, -1):
            if num//2**i:
                patterns[pattern_list[i]] = '1'
                num = num - 2**i
            else:
                patterns[pattern_list[i]] = '0'
        return patterns
    
    def next_line(self, line):
        lin1 = ''
        for i in range(len(line)):
            if i < len(line) - 1:
                p = line[i-1] + line[i] + line[i+1]
            else:
                p = line[i-1] + line[i] + line[0]
            
            lin1 = lin1 + self.rule()[p]
        return lin1
    
    def show(self, sqr):
        for char in sqr:
            if char == '0':
                print('.', end=' ')
            elif char == '1':
                print('*', end=' ')
        print()  # Add a newline at the end

    def calc(self, h=8):
        self.h = h
        cell_sq = []
        cell_sq.append(self.lin0)
        
        for i in range(self.h):
            if i < self.h - 1:
                cell_sq.append(self.next_line(cell_sq[i]))
            #print(cell_sq[i])
            self.show(cell_sq[i])


ac = AutoCell()
ac.calc(50)