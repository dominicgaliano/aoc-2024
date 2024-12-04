# Day 1

My initial thought was: "I'm going to be so clever and just subtract elements as they are read, there should be no difference between this and sorting it right?"

This thought would be correct if we were only finding the sum or difference.

```
(Sum(left_i - right_i) for i = 0 -> n) == (Sum(left_i) - Sum(right_i) for i = 0 -> n)
```

However, because this problem is asking for the distance (which really means absolute value), the logic really becomes:

```
Sum((left_i - right_i) if left_i > right_i else (right_i - left_i)) for i = 0 -> n
```

Because of this conditional branch, the pairing of left and right indexes matters.
