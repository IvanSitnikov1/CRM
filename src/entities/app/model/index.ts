import { defineStore } from 'pinia'
import type { IBookModel, IBook } from './types'

export const useAppModel = defineStore({
  id: 'book',

  state: () =>
    <IBookModel>{
      showNavigation: false,
      showFab: false,
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
      console.log(this.showNavigation)
      this.showNavigation = !this.showNavigation;
    },
    updateShowMenu(value: boolean): void {
      this.showNavigation = value;
    },
    updateShowFab(value: boolean): void {
      this.showFab = value;
    },
    updateShowSupport(value: boolean): void {
      this.showSupport = value;
    },
  }
})
