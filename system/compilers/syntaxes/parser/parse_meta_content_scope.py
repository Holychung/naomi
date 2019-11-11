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

from .ast import SetMetaContentScope
from .make_contextual_statement import make_contextual_statement


def parse_meta_content_scope(syntax, context, raw):
    statement = make_contextual_statement(
        SetMetaContentScope(),
        syntax,
        context,
        raw,
    )
    statement.value = raw['meta_content_scope']
    return statement
