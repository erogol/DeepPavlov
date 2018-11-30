# originally based on https://github.com/allenai/bilm-tf/blob/master/bilm/data.py

<<<<<<< HEAD
# Copyright 2017 Neural Networks and Deep Learning lab, MIPT
=======
# Modifications copyright 2017 Neural Networks and Deep Learning lab, MIPT
>>>>>>> dev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Union, List, Tuple
<<<<<<< HEAD

from pathlib import Path
import numpy as np
from itertools import chain
from collections import Counter, OrderedDict
=======
from itertools import chain
from pathlib import Path
from collections import Counter, OrderedDict

import numpy as np
>>>>>>> dev
from overrides import overrides

from deeppavlov.core.common.registry import register
from deeppavlov.core.common.errors import ConfigError
from deeppavlov.core.common.log import get_logger
from deeppavlov.core.models.estimator import Estimator

log = get_logger(__name__)

<<<<<<< HEAD
=======
StrUTF8EncoderInfo = Union[List[str], List['StrUTF8EncoderInfo']]

>>>>>>> dev

@register('str_utf8_encoder')
class StrUTF8Encoder(Estimator):
    """Component for encoding all strings to utf8 codes

<<<<<<< HEAD

=======
>>>>>>> dev
    Args:
        max_word_length: Max length of words of input and output batches.
        pad_special_char_use: Whether to use special char for padding  or not.
        word_boundary_special_char_use: Whether to add word boundaries by special chars or not.
        sentence_boundary_special_char_use: Whether to add word boundaries by special chars or not.
        reversed_sentense_tokens: Whether to use reversed sequences of tokens or not.
        bos: Name of a special token of the begin of a sentence.
        eos: Name of a special token of the end of a sentence.
    """
    def __init__(self, 
<<<<<<< HEAD
                 max_word_length:int = 50,
                 pad_special_char_use:bool = False,
                 word_boundary_special_char_use:bool = False,
                 sentence_boundary_special_char_use:bool = False,
                 reversed_sentense_tokens:bool = False,
                 bos:str = '<S>',
                 eos:str = '</S>',
                 **kwargs):
=======
                 max_word_length: int = 50,
                 pad_special_char_use: bool = False,
                 word_boundary_special_char_use: bool = False,
                 sentence_boundary_special_char_use: bool = False,
                 reversed_sentense_tokens: bool = False,
                 bos: str = '<S>',
                 eos: str = '</S>',
                 **kwargs) -> None:
>>>>>>> dev
        super().__init__(**kwargs)

        if word_boundary_special_char_use and max_word_length < 3:
                    raise ConfigError(f"`max_word_length` should be more than 3!")
        if max_word_length < 1:
                    raise ConfigError(f"`max_word_length` should be more than 1!")

        self._max_word_length = max_word_length
        self._reverse = reversed_sentense_tokens

<<<<<<< HEAD

=======
>>>>>>> dev
        self._pad_special_char_use = pad_special_char_use
        self._word_boundary_special_char_use = word_boundary_special_char_use
        self._sentence_boundary_special_char_use = sentence_boundary_special_char_use

        # char ids 0-255 come from utf-8 encoding bytes
        # assign 256-300 to special chars
        self.bos_char = 256  # <begin sentence>
        self.eos_char = 257  # <end sentence>
        self.bow_char = 258  # <begin word>
        self.eow_char = 259  # <end word>
<<<<<<< HEAD
        self.pad_char = 260 # <padding>

        self._len = 261 # an upper bound of all indexes
=======
        self.pad_char = 260  # <padding>

        self._len = 261  # an upper bound of all indexes
>>>>>>> dev

        # the charcter representation of the begin/end of sentence characters
        def _make_bos_eos(indx):
            indx = np.array([indx], dtype=np.int32)
            if self._word_boundary_special_char_use:
<<<<<<< HEAD
                code = np.pad(indx, (1,1), 'constant', constant_values=(self.bow_char,self.eow_char))
            else:
                code = indx
            if self._pad_special_char_use:
                code = np.pad(code, (0,self._max_word_length - code.shape[0]), 'constant', constant_values=(self.pad_char))
=======
                code = np.pad(indx, (1, 1), 'constant', constant_values=(self.bow_char, self.eow_char))
            else:
                code = indx
            if self._pad_special_char_use:
                code = np.pad(code, (0, self._max_word_length - code.shape[0]), 'constant', 
                              constant_values=(self.pad_char))
>>>>>>> dev
            else:
                pass
            return code
        
        self.bos_chars = _make_bos_eos(self.bos_char)
        self.eos_chars = _make_bos_eos(self.eos_char)

        if self._sentence_boundary_special_char_use:
<<<<<<< HEAD
            self._eos_chars =  [self.eos_chars]
            self._bos_chars =  [self.bos_chars]
        else:
            self._eos_chars =  []
            self._bos_chars =  []
=======
            self._eos_chars = [self.eos_chars]
            self._bos_chars = [self.bos_chars]
        else:
            self._eos_chars = []
            self._bos_chars = []
>>>>>>> dev

        if self.load_path:
            self.load()
        else:
            self.tokens = []
        self._word_char_ids = OrderedDict()

        for token in self.tokens:
            self._word_char_ids[token] = self._convert_word_to_char_ids(token)
        self._word_char_ids[bos] = self.bos_chars
        self._word_char_ids[eos] = self.eos_chars

<<<<<<< HEAD
    def __call__(self, batch: Union[List[str], Tuple[str]]):
=======
    def __call__(self, batch: Union[List[str], Tuple[str]]) -> StrUTF8EncoderInfo:
>>>>>>> dev
        """Recursively search for strings in a list and utf8 encode

        Args:
            batch: a string or a list containing strings

        Returns:
            the same structure where all strings are utf8 encoded
        """
        if isinstance(batch, (list, tuple)):
            if isinstance(batch[-1], str):
                return self._encode_chars(batch)
            else:
                return [self(line) for line in batch]
        raise RuntimeError(f'The objects passed to the reverser are not list or tuple of str! '
<<<<<<< HEAD
                            f' But they are {type(batch)}.')

    @overrides
    def load(self):
=======
                           f' But they are {type(batch)}.')

    @overrides
    def load(self) -> None:
>>>>>>> dev
        if self.load_path:
            if self.load_path.is_file():
                log.info(f"[loading vocabulary from {self.load_path}]")
                self.tokens = []
                for ln in self.load_path.open('r', encoding='utf8'):
                    token = ln.strip().split()[0]
                    self.tokens.append(token)
            elif isinstance(self.load_path, Path):
                if not self.load_path.parent.is_dir():
                    raise ConfigError(f"Provided `load_path` for {self.__class__.__name__} doesn't exist!")
        else:
            raise ConfigError(f"`load_path` for {self} is not provided!")

    @overrides
<<<<<<< HEAD
    def save(self):
=======
    def save(self) -> None:
>>>>>>> dev
        log.info(f"[saving vocabulary to {self.save_path}]")
        with self.save_path.open('wt', encoding='utf8') as f:
            for token in self._word_char_ids.keys():
                f.write('{}\n'.format(token))
            
    @overrides
<<<<<<< HEAD
    def fit(self, *args):
=======
    def fit(self, *args) -> None:
>>>>>>> dev
        words = chain(*args)
        # filter(None, <>) -- to filter empty words
        freqs = Counter(filter(None, chain(*words)))
        for token, _ in freqs.most_common():
            if not(token in self._word_char_ids):
                self._word_char_ids[token] = self._convert_word_to_char_ids(token)

    def _convert_word_to_char_ids(self, word):

        code = np.zeros([self._max_word_length], dtype=np.int32)
        if self._pad_special_char_use:
            code[:] = self.pad_char
        if self._word_boundary_special_char_use:
<<<<<<< HEAD
            word_encoded = word.encode('utf-8', 'ignore')[:self._max_word_length-2]
=======
            word_encoded = word.encode('utf-8', 'ignore')[:self._max_word_length - 2]
>>>>>>> dev
            code[0] = self.bow_char

            for k, chr_id in enumerate(word_encoded, start=1):
                code[k] = chr_id

<<<<<<< HEAD
            code[len(word_encoded)+1] = self.eow_char
=======
            code[len(word_encoded) + 1] = self.eow_char
>>>>>>> dev
        else:
            word_encoded = word.encode('utf-8', 'ignore')[:self._max_word_length]

            for k, chr_id in enumerate(word_encoded):
                code[k] = chr_id

        if not self._pad_special_char_use:
            if self._word_boundary_special_char_use:
<<<<<<< HEAD
                code = code[:len(word_encoded)+2]
=======
                code = code[:len(word_encoded) + 2]
>>>>>>> dev
            else:
                code = code[:len(word_encoded)]
        return code

<<<<<<< HEAD


=======
>>>>>>> dev
    def _word_to_char_ids(self, word):
        if word in self._word_char_ids:
            return self._word_char_ids[word]
        else:
            return self._convert_word_to_char_ids(word)

    def _encode_chars(self, sentence):
<<<<<<< HEAD
        '''
        Encode the sentence as a white space delimited string of tokens.
        '''
        chars_ids = [self._word_to_char_ids(cur_word)
                    for cur_word in sentence]
        return self._wrap_in_s_char(chars_ids)


=======
        """
        Encode the sentence as a white space delimited string of tokens.
        """
        chars_ids = [self._word_to_char_ids(cur_word)
                     for cur_word in sentence]
        return self._wrap_in_s_char(chars_ids)

>>>>>>> dev
    def _wrap_in_s_char(self, chars_ids):
        chars_ids = chars_ids if self._pad_special_char_use else list(chars_ids)
        if self._reverse:
            ret = self._eos_chars + chars_ids + self._bos_chars
        else:
            ret = self._bos_chars + chars_ids + self._eos_chars
        return np.vstack(ret) if self._pad_special_char_use else ret
<<<<<<< HEAD
=======

>>>>>>> dev
    def __len__(self):
        return self._len

    @property
    def len(self):
<<<<<<< HEAD
        '''
        An upper bound of all indexes.
        '''
        return len(self)
=======
        """
        An upper bound of all indexes.
        """
        return len(self)
>>>>>>> dev
