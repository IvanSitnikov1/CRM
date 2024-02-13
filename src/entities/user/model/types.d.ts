export interface IBookModel {
  queryBooks: books_v1.Schema$Volume[]
  book: IBook
  favorites: IBook[]
  bookshelf: IBook[]
}

export interface IUserCard {
  image: string
  tag?: string
  job?: string
  fullName: string
  isBox?: boolean
  isWhite?: boolean
}
