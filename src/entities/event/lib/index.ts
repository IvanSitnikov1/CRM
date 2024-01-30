

export const getAuthorsWithComma = (authors: string[] | undefined): string =>
  authors ? authors?.join(', ') : ''

