from pa4 import *

def main():
    list = [3,4]
    list2 = [-1, -2]
    vec1 = Vec(list)
    vec2 = Vec(list2)
    print("Testing start:")
    print(f"Vec1: {vec1} \nVec2: {vec2}")
    print(f"Vec1 + Vec2 = {vec1 + vec2}")
    print(f"Vec1 - Vec2 = {vec1 - vec2}")
    print(f"Vec1 * Vec2 = {vec1 * vec2}")
    print(f"magnitude of Vec1 = {abs(vec1)}")


main()