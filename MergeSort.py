class MergeSort:
    def __init__(self, integerList):
        self.integerList = integerList

    def sort(self):
        if len(self.integerList) > 1:
            #find the middle of the array
            midPoint = len(self.integerList) // 2

            #build lists from middle to ends using the original list

            left_half = self.integerList[:midPoint]
            right_half = self.integerList[midPoint:]


            #sort both halves recursively
            left_sorter = MergeSort(left_half)
            right_sorter = MergeSort(right_half)
            left_sorted = left_sorter.sort()
            right_sorted = right_sorter.sort()

            #merge the sorted halves
            self.integerList = self.merge(left_sorted, right_sorted)

        #return the sorted list
        return self.integerList
    
    def merge(self, left, right):
        #create new empty list
        result = []
        i = 0
        j = 0

        #merge the sorted arrays into the empty array created earlier
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+= 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    def print_sorted_list(self):
        print("Executing Merge Sort on a List of Integers")
        print("Sorted integerList: ", self.integerList)

            
            