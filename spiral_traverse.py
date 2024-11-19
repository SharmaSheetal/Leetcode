def spirallyTraverse( mat):
        r, c = len(mat), len(mat[0])
        top,left,down,right=0,0,r-1,c-1
        d=0 # This will keep track of the direction in which we are moving
        result = []
        while top<=down and left<=right:
            if d==0:
                for i in range(left,right+1):
                    result.append(mat[top][i])
                top+=1
            if d==1:
                for i in range(top,down+1):
                    result.append(mat[i][right])
                right-=1
            if d==2:
                for i in range(right,left-1,-1):
                    result.append(mat[down][i])
                down-=1
            if d==3:
                for i in range(down,top-1,-1):
                    result.append(mat[i][left])
                left+=1
            d=(d+1)%4
                
    
        return result
# Alternate

def spiralOrder(mat):
    r, c = len(mat), len(mat[0])
    result = []
    for i in range((min(r, c) + 1) // 2):  # Loop runs for layers
        # Traverse from left to right
        for j in range(i, c - i):  # Shrink columns on both sides
            result.append(mat[i][j])

        # Traverse from top to bottom
        for k in range(i + 1, r - i):  # Shrink rows on both sides
            result.append(mat[k][c - 1 - i])

        # Traverse from right to left, only if there is a new bottom row
        if i < r - 1 - i:
            for l in range(c - 2 - i, i - 1, -1):  # Move from right to left
                result.append(mat[r - 1 - i][l])

        # Traverse from bottom to top, only if there is a new left column
        if i < c - 1 - i:
            for m in range(r - 2 - i, i, -1):  # Move from bottom to top
                result.append(mat[m][i])

    return result



"""

Time Complexity: O(m*n),
Auxiliary Space: O(1).
Space complexity: O(m*n)

"""
