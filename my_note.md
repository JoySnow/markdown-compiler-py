We'll match Context-Free Languages.
And avoid left-recursion Grammar.

left-recursion Grammar:
  A rule which calls itself before calling another rule or a terminal.
  eg:
  ```
  Foo = Foo "ab"
      | "ab"
  ```

Q: Why avoid left-recursion Grammar ?
A: One is because it's harder to implement.

eg: The implemenation of a left-recursive rule:
```ruby
def my_rule
  if my_rule # infinite loop here
    do something
  else
    do something else
  end
end
```

The good news is that;
  all grammars with left-recursion [can be written as a different equivalent grammar
without left-recursion](http://www.csd.uwo.ca/~moreno/CS447/Lectures/Syntax.html/node8.html).




## On Abstract Syntax Trees

The grammar: take input, and build a AST for it as the outcome.

Abstract Syntax Tree representation(AST):

For example, a markdown grammar might parse `hello __world__.` as:

```
                       [PARAGRAPH]
                           |
                           v
               +-------[SENTENCES] ---------+
               |             |              |
               v             v              v
          [TEXT="hello "] [BOLD="world"] [TEXT="."]
```


The thing about getting a tree out of a grammar is that we can remove ambiguity.

So, we rewrite the grammar to transforming a left-recursive grammar to a non-left-recursive
grammar .



## A simple Markdown grammar
Okay, enough theory, let's start coding already! This is the grammar we'll
implement:

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
