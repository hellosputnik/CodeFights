def htmlEndTagByStartTag(startTag):
    tag = startTag.split()[0][1:]
    tag = tag[:-1] if tag[-1] == ">" else tag
    return "</" + tag + ">"

