const supportedAttributes = new Set(['title', 'location', 'id'])
const stableIdPattern = /^[a-z0-9][a-z0-9._-]*$/

export function parseNotationFenceInfo(info) {
  const source = info.trim()
  const languageMatch = source.match(/^([^\s]+)(?:\s+([\s\S]*))?$/)
  if (!languageMatch) {
    return {
      language: '',
      attributes: {},
      hasMetadata: false,
      error: 'notation fence needs a language'
    }
  }

  const language = languageMatch[1].toLowerCase()
  const attributes = {}
  let rest = (languageMatch[2] || '').trim()
  const hasMetadata = rest.length > 0

  while (rest) {
    const match = rest.match(/^([A-Za-z][A-Za-z0-9_-]*)="([^"]*)"(?=\s|$)/)
    if (!match) {
      return {
        language,
        attributes,
        hasMetadata,
        error: `invalid notation attributes near: ${rest}`
      }
    }

    const [, name, rawValue] = match
    if (!supportedAttributes.has(name)) {
      return {
        language,
        attributes,
        hasMetadata,
        error: `unsupported notation attribute: ${name}`
      }
    }
    if (Object.hasOwn(attributes, name)) {
      return {
        language,
        attributes,
        hasMetadata,
        error: `duplicate notation attribute: ${name}`
      }
    }

    attributes[name] = rawValue.trim()
    rest = rest.slice(match[0].length).trimStart()
  }

  if (hasMetadata && !attributes.title) {
    return { language, attributes, hasMetadata, error: 'notation metadata needs title' }
  }
  if (hasMetadata && !attributes.location) {
    return { language, attributes, hasMetadata, error: 'notation metadata needs location' }
  }
  if (attributes.id && !stableIdPattern.test(attributes.id)) {
    return {
      language,
      attributes,
      hasMetadata,
      error: 'notation id must match [a-z0-9][a-z0-9._-]*'
    }
  }

  return { language, attributes, hasMetadata, error: null }
}
