export interface IBookModel {
  queryBooks: books_v1.Schema$Volume[]
  book: IBook
  favorites: IBook[]
  bookshelf: IBook[]
}

export interface ICardEmployee {
  id?: string | null
  name?: string
  job?: string
  image?: string
  isShadow: boolean
  isBorderRound: boolean
  isShowLine: boolean
}
