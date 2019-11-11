# Copyright 2019 The ASReview Authors. All Rights Reserved.
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


def is_pickle(fp):
    """Check file for pickle extension."""
    fp = str(fp)
    return fp.endswith('.pkl') or fp.endswith('.pickle')


def convert_list_type(x, to_type=int):
    """Convert elements in list to given type."""

    return list(map(to_type, x))
