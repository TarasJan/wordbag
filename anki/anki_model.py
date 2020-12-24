import genanki

AnkiModel = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card',
      'qfmt': '<p style="text-align:center;font-size:large;"><b>{{Question}}</b>',
      'afmt': '<p style="text-align:center;font-size:large;"><b>{{Question}}</b><hr id="answer"><p style="text-align:center;font-size:large;"><b>{{Answer}}</b></p>',
    },
  ])