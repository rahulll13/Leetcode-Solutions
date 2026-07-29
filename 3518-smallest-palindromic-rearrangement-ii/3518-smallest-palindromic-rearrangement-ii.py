class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Combination function
        def comb(n, r, max_value):
            if r > n:
                return 0
            r = min(r, n - r)
            
            result = 1
            for i in range(1, r + 1):
                result = result * (n - r + i) // i
                if result >= max_value:
                    return max_value
            return result
        
        # Permutation counter
        def count_perms(counts, positions, max_value):
            perms = 1
            remaining = positions
            
            for count in counts:
                ways = comb(remaining, count, max_value)
                perms *= ways
                if perms >= max_value:
                    return max_value
                remaining -= count
            return perms
        
        # Max limit
        max_perms_needed = k + 1
        
        # Character counts
        char_freq = [0] * 26
        for c in s:
            char_freq[ord(c) - ord('a')] += 1
        
        # Process characters
        middle = ""
        half_counts = []
        
        for i in range(26):
            if char_freq[i] % 2 == 1:
                middle = chr(ord('a') + i)
            half_counts.append(char_freq[i] // 2)
        
        # Half length
        half_len = sum(half_counts)
        
        # Total count
        total_palindromes = count_perms(half_counts, half_len, max_perms_needed)
        
        # Validate k
        if k > total_palindromes:
            return ""
        
        # Build the first half
        first_half = []
        for pos in range(half_len):
            for c in range(26):
                if half_counts[c] == 0:
                    continue
                
                # Try this character
                half_counts[c] -= 1
                
                # Count palindromes with this prefix
                palindromes_with_prefix = count_perms(
                    half_counts, half_len - pos - 1, max_perms_needed
                )
                
                if k > palindromes_with_prefix:
                    # Skip this character
                    k -= palindromes_with_prefix
                    half_counts[c] += 1
                else:
                    # Use this character
                    first_half.append(chr(ord('a') + c))
                    break
        
        # Build the full palindrome
        first_half_str = ''.join(first_half)
        result = first_half_str + middle + first_half_str[::-1]
        
        return result