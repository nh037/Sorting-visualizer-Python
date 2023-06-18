import time

def merge_sort(data, drawrectangle, delay):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, drawrectangle, delay)
        merge_sort(right_half, drawrectangle, delay)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
            drawrectangle(data, ['blue' if x == k-1 else 'red' for x in range(len(data))] )
            time.sleep(delay)

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
            drawrectangle(data, ['blue' if x == k-1 else 'red' for x in range(len(data))] )
            time.sleep(delay)

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            drawrectangle(data, ['blue' if x == k-1 else 'red' for x in range(len(data))] )
            time.sleep(delay)

    drawrectangle(data, ['blue' for x in range(len(data))])
