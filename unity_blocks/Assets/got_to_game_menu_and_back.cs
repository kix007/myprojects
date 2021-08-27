using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class got_to_game_menu_and_back : MonoBehaviour
{
    GameObject GameMenu;
    GameObject MainMenu;

    // Start is called before the first frame update
    void Start()
    {
        MainMenu = GameObject.FindGameObjectWithTag("MainMenu");   
        GameMenu = GameObject.FindGameObjectWithTag("GameMenu"); 

        GameMenu.SetActive(false);

    }

    // Update is called once per frame
    void Update()
    {
            
    }
}
