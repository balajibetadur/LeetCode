class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hash = {}
        for i in range(len(messages)):
            hash[senders[i]] = hash.get(senders[i], 0) + len(messages[i].split())

        max_len = 0
        max_sender = ''
        for curr_sender, curr_len in hash.items():
            # if tmp_len >= max_length: max_length_sender = max(max_length_sender, name)
            # max_length = max(tmpx_len, max_length)
            if curr_len >= max_len:
                if curr_len == max_len: max_sender = max(max_sender, curr_sender)
                else: max_sender = curr_sender
                max_len = curr_len
                

        return max_sender