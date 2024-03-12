interface options {
  value: string
  title: string
}

export interface ISelect {
  name: string
  title: string
  options: options[]
  isDisable?: boolean
  isMultipleSelect?: boolean
}
