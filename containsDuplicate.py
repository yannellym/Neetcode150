  #Try
  
    def containsDuplicate(self, nums):
   
        set_a = set(nums)
        
        if len(set_a) < len(nums):
            return True
        return False
  
  
  #ultimate solution
  
  def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
      
  # additional solution

  if len(set(nums)) == len(nums):
            return False
        return True
    
  # additional solution

     counter = dict()

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            if counter[i] > 1:
                return True
        return False
