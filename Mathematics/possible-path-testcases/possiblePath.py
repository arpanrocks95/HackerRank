

# Complete the solve function below.
def gcd (a,b) :
    r = 0
    i = 0
    while(b!= 0):
        r = a % b
        a = b
        b = r
    return a

def solve(a, b, x, y):
    if(gcd(a,b) == gcd(x,y)) :
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        abxy = input().split()

        a = int(abxy[0])

        b = int(abxy[1])

        x = int(abxy[2])

        y = int(abxy[3])

        result = solve(a, b, x, y)

        print(result)
