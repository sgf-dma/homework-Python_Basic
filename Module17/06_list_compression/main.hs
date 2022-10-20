
-- $ stack runghc main.hs
--

list :: [Int]
list = [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]

main :: IO ()
main = print $ zerosToTheEnd list

-- Rebuild in a single pass.
zerosToTheEnd :: [Int] -> [Int]
zerosToTheEnd xs = foldr go id xs []
  where
    go :: Int -> ([Int] -> [Int]) -> [Int] -> [Int]
    go x h zeros
      | x == 0      = h (0 : zeros)
      | otherwise   = x : h zeros

