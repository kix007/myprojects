using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class RandomItemPosition : MonoBehaviour
{
    public Image[] images;
    // Start is called before the first frame update
    void Start()
    {
        foreach (Image image in images)
        {
            image.sprite = image.sprite;
            Debug.Log(image);
        }
    }
}



//OLD CODE FOR POSITION RANDOMIZE
//foreach (GameObject block in items)
// {
//    int RandomNumber = Random.Range(0, positions.Length);
//   block.transform.position = positions[RandomNumber];
//}
//transform.position = positions[randomNumber];


