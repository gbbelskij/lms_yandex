def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    the_left = array[:mid]
    the_right = array[mid:]
    the_left = merge_sort(the_left)
    the_right = merge_sort(the_right)
    return merge(the_left, the_right)

def merge(the_left, the_right):
    res = []
    left = 0
    right = 0
    while left < len(the_left) and right < len(the_right):
        if the_left[left] < the_right[right]:
            res.append(the_left[left])
            left += 1
        else:
            res.append(the_right[right])
            right += 1
    res += the_left[left:]
    res += the_right[right:]
    return res
