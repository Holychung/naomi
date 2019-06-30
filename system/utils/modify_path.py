# Licensed under the Apache License, Version 2.0 (the “License”); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from .replace_path_base import replace_path_base
from .replace_path_ext import replace_path_ext


def modify_path(path, old_base, new_base, new_extension=None):
    path = replace_path_base(path, old_base, new_base)
    if new_extension is None:
      return path
    return replace_path_ext(path, new_extension)
