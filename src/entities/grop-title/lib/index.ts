import type { IBook } from '../index'

export const getAuthorsWithComma = (authors: string[] | undefined): string =>
  authors ? authors?.join(', ') : ''

