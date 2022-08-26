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
