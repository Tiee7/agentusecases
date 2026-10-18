const headings = new Set(['实际使用','实际使用的 Agent','使用工具','使用的 Agent','具体做法','他们做了什么','结果如何','值得知道','值得注意','需要知道的事','自行试用','自己试试','推荐工具','复制提示词','原始来源','Done with','What they did','How it went','Worth knowing','Try it yourself','Copy prompt','Original source']);

// Classify a line without changing its text, whitespace, or line ending.
export function archiveLines(body) {
  const tokens = body.split(/(\r\n|\n|\r)/);
  const lines = [];
  let hasTitle = false;
  for (let i = 0; i < tokens.length; i += 2) {
    const text = tokens[i], ending = tokens[i + 1] || '';
    if (!text && !ending) continue;
    const label = text.trim();
    const kind = !label ? 'blank' : !hasTitle ? 'title' : headings.has(label) ? 'heading' : 'paragraph';
    if (label) hasTitle = true;
    lines.push({text, ending, kind});
  }
  return lines;
}

// Only these constant separators enter set:html. Encoding CR prevents HTML's
// newline normalization from changing CRLF/CR source text in the browser DOM.
export const archiveEndings = Object.freeze({'': '', '\n': '\n', '\r': '&#13;', '\r\n': '&#13;\n'});
