# -*- coding: utf-8 -*-
"""
    DFA Algorithm   --> Class
    Functions:
        1.  Given text content
            Return Questionable words prediction

        2.  Given txt, output directory
            -   Create 8 categorised files in directory:
                (directory/TempCategory/XX_label.txt)

                XX_label:
                ["abuse", "ad", "cult", "drug", "lottery", "political", "violence"]

            -   Save un-categorised files in output.txt in directory:
                (directory/output.txt)
"""
import time
import pypinyin
from pypinyin import lazy_pinyin


class Node(object):
    def __init__(self, name='root'):
        self.name = name
        self.children = None
        self.flag = False

    def items(self):
        return self.children.items()

    def show(self, indent=0):
        """show tree to string"""
        tab = '    ' * (indent - 1) + ' |- ' if indent > 0 else ''
        print('%s%s' % (tab, self.name))
        for name, obj in self.items():
            if not obj.flag:
                obj.show(indent + 1)


class DFA(object):
    """
    Attribute:
        root:           save the DFA tree
        switch_memory:  decide if need to memorise the matched message
        message_memory: memorise a list of matched words

    Function:
        add_word:       add char to word tree
                        add end flag on the tree
        search:         scan and search word on the tree
                        if switch_memory ON
                            memorise the matched words
    N.B.:
        [:-1] represents that removing the last '\n' in the string nodes.
    """
    def __init__(self, wordlist, switch_memory=False, switch_pinyi=False):
        self.root = Node(name='root')
        self.switch_memory = switch_memory
        self.switch_pinyin = switch_pinyi
        self.message_memory = list()

        for line in wordlist:
            if self.switch_pinyin:
                self.add_word(''.join(lazy_pinyin(line, strict=False, style=pypinyin.NORMAL)))
            else:
                self.add_word(line)

    def add_word(self, word):
        if len(word) <= 0:
            return
        node = self.root
        for i in range(len(word)):
            if node.children is None:
                node.children = dict()
                node.children[word[i]] = Node(name=word[i])

            elif word[i] not in node.children:
                node.children[word[i]] = Node(name=word[i])

            node = node.children[word[i]]
        node.flag = True

    def search(self, msg):
        res = set()
        for msg_index in range(len(msg)):
            dict_cursor = self.root
            dict_cursor_index = msg_index
            while dict_cursor_index < len(msg) \
                    and dict_cursor.children is not None \
                    and msg[dict_cursor_index] in dict_cursor.children:
                if dict_cursor.flag:
                    res.add(msg[msg_index:dict_cursor_index])
                dict_cursor = dict_cursor.children[msg[dict_cursor_index]]
                dict_cursor_index += 1

            if dict_cursor.flag:
                res.add(msg[msg_index:dict_cursor_index])
                if self.switch_memory:
                    self.message_memory.append(str(msg))

        return list(res)

    def message_detected(self):
        return self.message_memory


def print_dfa_result(inputfile):
    """
    :param inputfile:   To-be-matched content
    :return:            None
                        print questionable words and its category
                        print execute time

    Method:             Read the file as a whole message('\n' removed)
                        Iterate each category labels
                        print results

    """
    with open(inputfile, 'r') as f:
        message = ''.join(f.readlines())

    start_time = time.time()

    labels = ["abuse", "ad", "cult", "drug", "lottery", "political", "sex", "violence"]
    for fn in labels:
        with open('GenerateMergeSet/' + fn + '.txt', 'r') as f:
            wordlist = f.readlines()
        dfadict = DFA(wordlist)
        bad_words = dfadict.search(message)
        if len(bad_words) > 0:
            print("Questionable Words： ", bad_words, "\nCategory： ", fn)
            print("*" * 60)
    end_time = time.time()
    print("Run Time: ", end_time - start_time)


if __name__ == '__main__':

    with open('GenerateMergeSet/' + 'abuse' + '.txt', 'r') as f:
        word_list = f.readlines()
    dfa_dict = DFA(word_list)

    dfa_dict.root.show()

    '''
    run_time = time.time()
    testfile = 'test_content.txt'
    print_dfa_result(testfile)
    '''
