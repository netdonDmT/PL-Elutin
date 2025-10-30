def nech():
    data = input().split()
    
    def process(index):
        if index >= len(data) or data[index] == '0':
            return
        print(data[index])
        if index + 2 < len(data):
            process(index + 2)
    
    process(0)

nech()