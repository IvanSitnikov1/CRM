class IosSelector {
  constructor(options) {
    let defaults = {
      el: "", // dom
      type: "infinite", // infinite 无限滚动，normal 非无限
      count: 20, // 圆环规格，圆环上选项个数，必须设置 4 的倍数
      sensitivity: 0.8, // 灵敏度
      source: [], // 选项 {value: xx, text: xx}
      value: null,
      onChange: null
    };
    this.selected = this.source[0];


    this.itemHeight = (this.elems.el.offsetHeight * 3) / this.options.count; // 每项高度

    this._init();
  }

  _init() {
    if (this.source.length) {
      this.value = this.value !== null ? this.value : this.source[0].value;
      this.select(this.value);
    }
  }


  _create(source) {

    // source 处理
    if (this.options.type === "infinite") {
      let concatSource = [].concat(source);
      while (concatSource.length < this.halfCount) {
        concatSource = concatSource.concat(source);
      }
      source = concatSource;
    }
  }


  _selectByScroll(scroll) {
    scroll = this._normalizeScroll(scroll) | 0;
    if (scroll > this.source.length - 1) {
      scroll = this.source.length - 1;
      this._moveTo(scroll);
    }
    this._moveTo(scroll);
    this.scroll = scroll;
    this.selected = this.source[scroll];
    this.value = this.selected.value;
    this.onChange && this.onChange(this.selected);
  }

  select(value) {
    for (let i = 0; i < this.source.length; i++) {
      if (this.source[i].value === value) {
        window.cancelAnimationFrame(this.moveT);
        // this.scroll = this._moveTo(i);
        let initScroll = this._normalizeScroll(this.scroll);
        let finalScroll = i;
        let t = Math.sqrt(Math.abs((finalScroll - initScroll) / this.a));
        this._animateToScroll(initScroll, finalScroll, t);
        setTimeout(() => this._selectByScroll(i));
        return;
      }
    }
    throw new Error(
      `can not select value: ${value}, ${value} match nothing in current source`
    );
  }

}
