import { Animate } from 'react-move';
import { easeExpInOut } from 'd3-ease';

/**
 * Creates an annimated box whose height can be set.
 * @param {{height: Number, maxHeight?: Number}} props - Height values to used for rendering box.
 * @returns A React functional component. 
 */
function BoxView(props) {

  const { maxHeight, height } = props;

  // Have not worried about making a lot of these properties configurable for this example but could easily do so using
  // the `props` property.
  return (<svg
    width="768"
    height="576"
    viewBox="0 0 203.2 152.4"
    version="1.1"
    id="svg5"
    xmlns="http://www.w3.org/2000/svg"
    xmlnssvg="http://www.w3.org/2000/svg">
    <defs
      id="defs2" />
    <g
      id="layer1">
      <Animate
        start={() => ({ height: 0 })}
        update={() => ({ 
          height: [Math.min(height, isNaN(maxHeight) ? 100 : maxHeight)],
          timing: { duration: 500, ease: easeExpInOut},
        })}
        >
        {state => {
          return (
            <rect
          fill='#ffd257'
          strokeWidth={0.3}
          id="rect111"
          width="200"
          x="0"
          y="0"
          {...state} />
          );
        }}
      </Animate>
    </g>
  </svg>
  );
}

export default BoxView;