import { defineStore } from 'pinia'
import type { IBookModel, IBook } from './types'

export const useAppModel = defineStore({
  id: 'book',

  state: () =>
    <IBookModel>{
      showNavigation: false,
      showSupport: false,
    },

  getters: {
    isBookInFavorites() {
      return (id: string | undefined | null): boolean =>
        this.favorites.some((item: IBook) => item.id === id)
    },
  },

  actions: {
    toggleShowMenu(): void {
      this.showNavigation = !this.showNavigation;
    },
    updateShowMenu(value: boolean): void {
      this.showNavigation = value;
    },
    updateShowSupport(value: boolean): void {
      this.showSupport = value;
    },
  }
})
