import { defineStore } from 'pinia'
export type IModalType = 'project' | 'task' | 'event' | 'request' | 'employee' | 'folder' | 'all'

export const useModalStore = defineStore('counter', () => {
  const state = ref({
    showAdd: false,
    showAddProject: false,
    showAddTask: false,
    showAddEvent: false,
    showAddRequest: false,
    showAddEmployee: false,
    showAddFolder: false,
  })

  const openModalAdd = (type: IModalType) => {
    switch (type) {
      case 'employee':
        state.value.showAddEmployee = true
        break
      case 'all':
        state.value.showAdd = true
        break
      case 'event':
        state.value.showAddEvent = true
        break
      case 'folder':
        state.value.showAddFolder = true
        break
      case 'project':
        state.value.showAddProject = true
        break
      case 'request':
        state.value.showAddRequest = true
        break
      case 'task':
        state.value.showAddTask = true
        break
      default:
        throw new Error(`Error to open modal type ${modal.type}`)
    }
  }

  return {
    state,
    openModalAdd,
  }
})
