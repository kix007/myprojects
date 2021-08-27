using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class CanvasResizer : MonoBehaviour {
 
    public Camera camera;
    public float ratio = 0.49f;
 
    void Update () {
        RectTransform objectRectTransform = this.gameObject.GetComponent<RectTransform>();
        objectRectTransform.SetSizeWithCurrentAnchors(RectTransform.Axis.Horizontal, Screen.width);
        objectRectTransform.SetSizeWithCurrentAnchors(RectTransform.Axis.Vertical, Screen.height);
        this.camera.orthographicSize = Screen.height * this.ratio;
    }
}
