def break_into_lines(text, max_line_length):
    lines = []
    current_line = ""
    
    # Split the text into words
    words = text.split()
    
    for word in words:
        # Check if adding the current word exceeds the maximum line length
        if len(current_line + " " + word) > max_line_length:
            # Add the current line to the list of lines
            lines.append(current_line.strip())
            current_line = ""
        
        current_line += word + " "
    
    # Add the last line to the list of lines
    lines.append(current_line.strip())
    
    # Join the lines with line breaks
    return "\n".join(lines)