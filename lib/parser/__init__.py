"""
# A simple Markdown grammar

    Body               := Paragraph*

    Paragraph          := SentenceAndNewline
                        | SentenceAndEOF

    SentenceAndNewline := Sentence+ NEWLINE NEWLINE

    SentencesAndEOF    := Sentence+ NEWLINE EOF
                        | Sentence+ EOF

    Sentence           := EmphasizedText
                        | BoldText
                        | Text

    EmphasizedText     := UNDERSCORE BoldText UNDERSCORE

    BoldText           := UNDERSCORE UNDERSCORE TEXT UNDERSCORE UNDERSCORE
                        | STAR STAR TEXT STAR STAR

    Text               := TEXT
"""
