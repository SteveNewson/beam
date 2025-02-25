#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# beam-playground:
#   name: WordCountKata
#   description: Task from katas to create a pipeline that counts the number of words.
#   multifile: false
#   context_line: 29
#   categories:
#     - Combiners
#   complexity: BASIC
#   tags:
#     - count
#     - map
#     - combine
#     - string
#     - number

import apache_beam as beam

from log_elements import LogElements

lines = [
    "apple orange grape banana apple banana",
    "banana orange banana papaya"
]

with beam.Pipeline() as p:

  (p | beam.Create(lines)
     | beam.FlatMap(lambda sentence: sentence.split())
     | beam.combiners.Count.PerElement()
     | beam.MapTuple(lambda k, v: k + ":" + str(v))
     | LogElements())
