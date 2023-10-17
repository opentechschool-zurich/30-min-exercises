import Data.List.NonEmpty

majority :: Eq a => NonEmpty a -> a
majority (x :| xs) = inner_majority 1 x xs
  where
    inner_majority :: Eq a => Int -> a -> [a] -> a
    inner_majority _ m [] = m
    inner_majority 0 _ (x:xs) = inner_majority 1 x xs
    inner_majority i m (x:xs) | m == x = inner_majority (i + 1) m xs
    inner_majority i m (_:xs) = inner_majority (i - 1) m xs
